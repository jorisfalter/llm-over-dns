


#!/usr/bin/env python3
"""
Interactive Chat Interface for ch.at DNS LLM
Based on the ch.at server from the Twitter post.
"""

import subprocess
import sys

class DNSChat:
    def __init__(self, server="ch.at", port="53"):
        self.server = server
        self.port = port
        
    def query_llm(self, question):
        """Send question to LLM over DNS and return clean response."""
        try:
            # For ch.at, the format is different - question goes directly as subdomain
            # Example: dig @ch.at "what is golang" TXT +short
            
            # Execute dig command for ch.at server
            cmd = [
                "dig", f"@{self.server}",
                question, "TXT", "+short"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            
            if result.returncode == 0 and result.stdout.strip():
                # Clean up the response (remove quotes, join multiple lines)
                response = result.stdout.strip()
                # Remove quotes and join multiple TXT records
                lines = [line.strip('"') for line in response.split('\n') if line.strip()]
                return ' '.join(lines)
            else:
                return "❌ No response from DNS server"
                
        except subprocess.TimeoutExpired:
            return "⏰ Query timed out"
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def start_chat(self):
        """Start interactive chat session."""
        print("🤖 ch.at DNS Chat Interface")
        print("=" * 40)
        print(f"📡 Connected to: {self.server}")
        print("💬 Type your questions below (or 'quit' to exit)")
        print("🔧 Example: what is golang")
        print("=" * 40)
        print()
        
        while True:
            try:
                # Get user input
                question = input("🙋 You: ").strip()
                
                if not question:
                    continue
                    
                if question.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                if question.lower() in ['help', '?']:
                    self.show_help()
                    continue
                
                # Show thinking indicator
                print("🤔 Thinking...", end="", flush=True)
                
                # Query the LLM
                response = self.query_llm(question)
                
                # Clear thinking indicator and show response
                print("\r" + " " * 15 + "\r", end="")  # Clear the thinking line
                print(f"🤖 AI: {response}")
                print()
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break
    
    def show_help(self):
        """Show help information."""
        print()
        print("📖 Help:")
        print("  • Ask any question in natural language")
        print("  • Type 'quit' or 'exit' to leave")
        print("  • Type 'help' or '?' for this message")
        print("  • Examples:")
        print("    - what is golang")
        print("    - explain python")
        print("    - tell me a joke")
        print("    - how do computers work")
        print()

def main():
    """Main function to start the chat interface."""
    if len(sys.argv) > 1:
        # Single query mode
        question = ' '.join(sys.argv[1:])
        chat = DNSChat()
        print(f"🔍 Asking: {question}")
        print()
        response = chat.query_llm(question)
        print(f"🤖 {response}")
    else:
        # Interactive chat mode
        chat = DNSChat()
        chat.start_chat()

if __name__ == "__main__":
    main() 