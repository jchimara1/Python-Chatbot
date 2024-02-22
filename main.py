# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:54:24 2023

@author: Justice
"""

import json 
from difflib import get_close_matches





def load_data(file_path: str):
    
   '''
   @param file_path is the string pointing to the json file that will serve as the brain for this chatbot
   ''' 
   with open(file_path, "r") as file: 
    data = json.loads(file.read())
    return data


def save_knowledge(file_path:str, data: dict):
    
    ''' 
    @param file_path = str(file path) 
    @param data = dict 
    this ithe function that will save inputs and begin the training of the chatbot '''
    
    with open(file_path, "w") as file :
         json.dump(data, file, indent=2)
         
         
         
def find_best_match(user_question:str, question:list[str]):
 matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)         
 return matches[0] if matches else None


def get_answer_for_question(question:str, knowledge_base:dict):
    for q in knowledge_base["question"]:
        if q["question"] == question:
            return q["answer"]
            
        
        
def chat_bot():
    
    knowledge_base: dict = load_data(r"knowledge_base.json")
    while True:
      user_input: str = input("You:") 

      if user_input.lower() == "quit":
        break       
    
    
      best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["question"]])
      
      if best_match:
          answer:str = get_answer_for_question(best_match, knowledge_base)
          print(f'bot: {answer}')
          
      else:
          print('Bot: I dont know that answer yet, can you teach me\n')
          new_answer:str = input("type the answer or skip\n")
          
          if new_answer != "skip":
              knowledge_base["question"].append({"question":user_input, "answer": new_answer})
              save_knowledge("knowledge_base.json", knowledge_base)
              print("bot: Thank you! i learned a know response")
              
              
              
if __name__ == '__main__':
   chat_bot()              