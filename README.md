# LLM-over-DNS 🌐🤖

A real DNS server that you can send LLM queries to and get AI responses back through DNS TXT records!

Inspired by: https://x.com/levelsio/status/1952861177731793324

dig @ch.at "what is golang" TXT +short

dig@llm.pieter.com -p 9000 "what is the meaning of life" TXT +short

## Limitations

- DNS TXT records have size limits, so very long responses are chunked
- Only works with TXT queries
- No caching (each query hits the OpenAI API)

## Easy-to-Use Interfaces 🎯

The raw `dig` command is too clunky! Here are much better ways to use the **real live ChatGPT over DNS**:

### 💬 **Interactive Chat Interface**

For longer conversations:

```bash
python3 chat.py
```

This opens a ChatGPT-like terminal interface:

```
🤖 LLM-over-DNS Chat Interface
========================================
📡 Connected to: llm.pieter.com:9000
💬 Type your questions below (or 'quit' to exit)
========================================

🙋 You: what is python?
🤔 Thinking...
🤖 AI: Python is a high-level programming language known for its simplicity and readability. Great for beginners!

🙋 You: tell me a joke
🤔 Thinking...
🤖 AI: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

🙋 You: quit
👋 Goodbye!
```

### ⚡ **Single Query Mode**

You can also use the chat script for one-off questions:

```bash
python chat.py "explain machine learning"
```

### **Technical Limits:**

- **Total domain name**: 253 characters maximum
- **Practical limit**: ~200 characters for questions
- **After removing `.llm.pieter.com`**: ~185 characters for your actual question

### **Examples:**

| Length            | Example                                                                          | Works?            |
| ----------------- | -------------------------------------------------------------------------------- | ----------------- |
| Short (10 chars)  | `what is AI`                                                                     | ✅                |
| Medium (50 chars) | `explain machine learning algorithms in detail`                                  | ✅                |
| Long (150+ chars) | `this is a very long question about artificial intelligence and how it works...` | ❌ Gets truncated |

### **Best Practices:**

- ✅ **Keep prompts under 150 characters**
- ✅ **Use concise, specific questions**
- ✅ **Avoid unnecessary words**
- ❌ **Don't write essays in the prompt**

## License

MIT License - Feel free to use and modify!
