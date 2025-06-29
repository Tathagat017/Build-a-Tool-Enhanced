"""
Tool-Enhanced Reasoning Script

This script takes natural language queries and uses an LLM to:
1. Interpret the query using chain-of-thought reasoning
2. Call external tools when necessary
3. Combine results to produce a final answer
"""

import os
import re
import json
from typing import Dict, Any, List, Tuple
from dotenv import load_dotenv
from openai import OpenAI

from tools.math_tools import MATH_TOOLS
from tools.string_tools import STRING_TOOLS

# Load environment variables
load_dotenv()

class ToolEnhancedReasoner:
    def __init__(self):
        """Initialize the reasoner with OpenAI client and tools."""
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.tools = {**MATH_TOOLS, **STRING_TOOLS}
        
    def create_reasoning_prompt(self, query: str) -> str:
        """Create a prompt that encourages tool usage and step-by-step reasoning."""
        available_tools = "\n".join([f"- {name}: {func.__doc__}" for name, func in self.tools.items()])
        
        prompt = f"""You are an intelligent assistant that can solve problems step-by-step and use tools when needed.

Available Tools:
{available_tools}

Instructions:
1. Break down the problem into logical steps using chain-of-thought reasoning
2. Identify if you need to use any tools to solve parts of the problem
3. When you need a tool, format it as: TOOL_CALL: tool_name(arguments)
4. After tool calls, continue your reasoning with the results
5. Provide a clear final answer

Query: {query}

Think step by step and use tools when necessary:"""
        
        return prompt

    def parse_tool_calls(self, text: str) -> List[Tuple[str, str, List]]:
        """Parse tool calls from LLM response."""
        tool_calls = []
        # Pattern to match TOOL_CALL: function_name(arguments)
        pattern = r'TOOL_CALL:\s*(\w+)\((.*?)\)'
        matches = re.findall(pattern, text)
        
        for tool_name, args_str in matches:
            if tool_name in self.tools:
                # Parse arguments
                args = []
                if args_str.strip():
                    # Handle different argument formats
                    try:
                        # Try to split by comma and convert to appropriate types
                        arg_parts = [arg.strip().strip('\'"') for arg in args_str.split(',')]
                        for arg in arg_parts:
                            # Try to convert to number, otherwise keep as string
                            try:
                                if '.' in arg:
                                    args.append(float(arg))
                                else:
                                    args.append(int(arg))
                            except ValueError:
                                args.append(arg)
                    except:
                        args = [args_str.strip().strip('\'"')]
                
                tool_calls.append((tool_name, args_str, args))
        
        return tool_calls

    def execute_tool(self, tool_name: str, args: List) -> Any:
        """Execute a tool with given arguments."""
        if tool_name not in self.tools:
            return f"Error: Tool '{tool_name}' not found"
        
        try:
            result = self.tools[tool_name](*args)
            return result
        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a natural language query with tool-enhanced reasoning."""
        print(f"\n🤔 Processing query: {query}")
        print("=" * 60)
        
        # Step 1: Get initial reasoning from LLM
        prompt = self.create_reasoning_prompt(query)
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800,
                temperature=0.1
            )
            
            initial_reasoning = response.choices[0].message.content
            print("🧠 Initial Reasoning:")
            print(initial_reasoning)
            print()
            
        except Exception as e:
            return {
                "query": query,
                "error": f"Failed to get initial reasoning: {str(e)}",
                "reasoning_steps": [],
                "tools_used": [],
                "final_answer": "Error occurred during processing"
            }

        # Step 2: Parse and execute tool calls
        tool_calls = self.parse_tool_calls(initial_reasoning)
        tools_used = []
        tool_results = {}
        
        if tool_calls:
            print("🔧 Tool Calls Detected:")
            for tool_name, args_str, args in tool_calls:
                print(f"  - Calling {tool_name}({args_str})")
                result = self.execute_tool(tool_name, args)
                tool_results[f"{tool_name}({args_str})"] = result
                tools_used.append({
                    "tool": tool_name,
                    "arguments": args_str,
                    "result": result
                })
                print(f"    Result: {result}")
            print()
        else:
            print("🔧 No tools needed for this query")
            print()

        # Step 3: Get final reasoning with tool results
        if tool_results:
            tool_results_text = "\n".join([f"{call}: {result}" for call, result in tool_results.items()])
            final_prompt = f"""Based on your previous reasoning and the following tool results, provide a clear final answer:

Previous reasoning:
{initial_reasoning}

Tool results:
{tool_results_text}

Please provide a concise final answer to the original query: {query}"""

            try:
                final_response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": final_prompt}],
                    max_tokens=300,
                    temperature=0.1
                )
                
                final_reasoning = final_response.choices[0].message.content
                print("🎯 Final Reasoning:")
                print(final_reasoning)
                
            except Exception as e:
                final_reasoning = f"Error getting final reasoning: {str(e)}"
        else:
            final_reasoning = initial_reasoning

        # Extract final answer
        final_answer = self.extract_final_answer(final_reasoning)
        
        print(f"\n✅ Final Answer: {final_answer}")
        print("=" * 60)

        return {
            "query": query,
            "reasoning_steps": [initial_reasoning, final_reasoning] if tool_results else [initial_reasoning],
            "tools_used": tools_used,
            "final_answer": final_answer
        }

    def extract_final_answer(self, text: str) -> str:
        """Extract the final answer from the reasoning text."""
        # Look for common final answer patterns
        patterns = [
            r"final answer[:\s]+(.+?)(?:\n|$)",
            r"answer[:\s]+(.+?)(?:\n|$)",
            r"therefore[,\s]+(.+?)(?:\n|$)",
            r"so[,\s]+(.+?)(?:\n|$)"
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # If no pattern found, return the last sentence
        sentences = text.strip().split('.')
        return sentences[-1].strip() if sentences else text.strip()


def main():
    """Main function to run the tool-enhanced reasoning script."""
    print("🚀 Tool-Enhanced Reasoning Script")
    print("Ask me anything! I can use mathematical and string analysis tools to help.")
    print("Type 'quit' to exit.\n")
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        print("Example: OPENAI_API_KEY=your_api_key_here")
        return
    
    reasoner = ToolEnhancedReasoner()
    
    # Example queries for demonstration
    example_queries = [
        "What's the square root of the average of 18 and 50?",
        "How many vowels are in the word 'Multimodality'?",
        "Is the number of letters in 'machine' greater than the number of vowels in 'reasoning'?",
        "What's 15 factorial divided by 10 factorial?",
        "How many consonants are in the longest word: 'artificial', 'intelligence', or 'reasoning'?"
    ]
    
    print("Example queries you can try:")
    for i, query in enumerate(example_queries, 1):
        print(f"{i}. {query}")
    print()
    
    while True:
        try:
            query = input("Enter your query (or 'quit' to exit): ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not query:
                print("Please enter a query.")
                continue
            
            # Process the query
            result = reasoner.process_query(query)
            
            # Ask if user wants to see detailed breakdown
            show_details = input("\nWould you like to see the detailed breakdown? (y/n): ").strip().lower()
            if show_details in ['y', 'yes']:
                print("\n📊 Detailed Breakdown:")
                print(f"Query: {result['query']}")
                print(f"Tools Used: {len(result['tools_used'])}")
                for tool in result['tools_used']:
                    print(f"  - {tool['tool']}({tool['arguments']}) = {tool['result']}")
                print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main() 