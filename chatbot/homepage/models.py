# from django.db import models

# # Create your models here.
# from typing import List


# class Message:
#     role: str
#     content: str
#     refusal: None
#     reasoning: None

#     def __init__(self, role: str, content: str, refusal: None, reasoning: None) -> None:
#         self.role = role
#         self.content = content
#         self.refusal = refusal
#         self.reasoning = reasoning

#     def __str__(self):
#         return 

# class Choice:
#     logprobs: None
#     finish_reason: str
#     native_finish_reason: str
#     index: int
#     message: Message

#     def __init__(self, logprobs: None, finish_reason: str, native_finish_reason: str, index: int, message: Message) -> None:
#         self.logprobs = logprobs
#         self.finish_reason = finish_reason
#         self.native_finish_reason = native_finish_reason
#         self.index = index
#         self.message = message


# class Usage:
#     prompt_tokens: int
#     completion_tokens: int
#     total_tokens: int

#     def __init__(self, prompt_tokens: int, completion_tokens: int, total_tokens: int) -> None:
#         self.prompt_tokens = prompt_tokens
#         self.completion_tokens = completion_tokens
#         self.total_tokens = total_tokens


# class Welcome5:
#     id: str
#     provider: str
#     model: str
#     object: str
#     created: int
#     choices: List[Choice]
#     usage: Usage

#     def __init__(self, id: str, provider: str, model: str, object: str, created: int, choices: List[Choice], usage: Usage) -> None:
#         self.id = id
#         self.provider = provider
#         self.model = model
#         self.object = object
#         self.created = created
#         self.choices = choices
#         self.usage = usage
