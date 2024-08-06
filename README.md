
# LLM Logger

LLM Logger is a simple and reusable logging library designed to log system prompts, user prompts, and responses in a standardized format. This library is ideal for logging interactions with large language models (LLMs) such as GPT-4.

## Features

- Logs system prompts, user prompts, and responses
- Includes timestamp and function name in the logs
- Easy to integrate into any Python project

## Installation

To use the `LLM Logger`, clone the repository from GitHub:

```sh
git clone https://github.com/enesbasbug/llm_logger_library
cd llm_logger
```

### Sample usage
```python
system_propmt, user_prompt = extract_prompts(
    prompt_file_path,
    **replacements
)
response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_propmt
        },
        {
            "role": "user",
            "content": user_prompt
        },
    ],
    temperature=1
)

# Extracting and cleaning the GPT response
result = response.choices[0].message.content.strip()
activate_llm_logger(user_prompt, system_propmt, response)
```

### Sample output of the log file
```
2024-08-06 22:32:02 - Function: story_generator
System Prompt:
You are a helpful assistant.
User Prompt:
I'll give you some data that you can write a story about. Return your answer in markdown format. Output should be short and concise.

Here is the data:
A shy, young woman unexpectedly bumps into her soulmate (literally bumps into him). In film, this is called the “meet cute,” when the hero bumps into the heroine in the coffee shop or the department store or the hallway, knocking her books to the floor, and forcing them into conversation.

Response:
ChatCompletion(id='chatcmpl-9tN0eWLxecaIZ4HIuI', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# A Serendipitous Encounter\n\nElena was a creature of habit, always choosing the same coffee shop every Saturday morning. Today, she was focused on her latte art, her thoughts swirling like the froth on her cup. As she stepped backward to admire her masterpiece, she collided with someone—a complete stranger. \n\n“Whoa!” the voice exclaimed, filled with warmth. Elena turned to see a young man, his hazel eyes wide with surprise. In a flurry, he knelt to help gather her scattered belongings.\n\n“I’m so sorry!” Elena stammered, cheeks flushing pink as she watched him pick up her fallen books. “I didn’t see you there.”\n\n“No harm done,” he chuckled, a smile breaking across his face. “Though I’m quite glad I could dive into your world of literature.” He handed her a volume of poetry, its pages slightly crinkled from the shock.\n\nAs their fingers brushed against each other, a spark ignited in the space between them—something electric, undeniable. This was not just an accident; this was fate at play. \n\nThey spent the next hour lost in conversation, laughter cascading like the coffee brewing behind the counter. In that little café, amid the bustling crowd, Elena discovered the missing piece of her heart.\n\nTheir unplanned meeting became the first chapter of their beautiful story—a perfect example of a “meet cute” blossoming into something far more profound than either could have ever imagined.', role='assistant', function_call=None, tool_calls=None, refusal=None))], created=1722983512, model='gpt-4o-mini-2024-07-18', object='chat.completion', system_fingerprint='fp_507c94asdf1', usage=CompletionUsage(completion_tokens=296, prompt_tokens=109, total_tokens=405))

------
```
