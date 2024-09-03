import json, re

class Gpt2md:
    def __init__(self, input_file:str, output_folder:str=".", verbose:bool=False):
        self.input_file = input_file
        self.output_folder = output_folder
        self.verbose = verbose
    
    def parse(self):
        data_file = open(self.input_file, "r", encoding="utf-8").read()
        json_data = json.loads(data_file)

        for conversation in json_data:
            conversation_title = re.sub('[<>"/\\|?*]', "-", conversation["title"])
            conversation_title = re.sub(':', " -", conversation_title)
            conversation_to_markdown(get_conversation_messages(conversation), f'{self.output_folder}/{conversation_title}.md')

            if self.verbose:
                print(f"Converted '{conversation['title']}' to markdown")

def get_conversation_messages(conversation: dict):
    data = {
        "title": conversation["title"],
        "messages": []
    }

    current_node = conversation["current_node"]
    
    while current_node is not None:
        node = conversation["mapping"].get(current_node)
        if not node:
            break
        
        message = node.get("message")
        if not message:
            break
        
        content = message.get("content", {})
        content_type = content.get("content_type")
        content_parts = content.get("parts", [])
        author_role = message.get("author", {}).get("role")
        is_user_system_message = message.get("metadata", {}).get("is_user_system_message", False)

        if (content_type == "text" and 
            content_parts and 
            content_parts[0] and 
            (author_role != "system" or is_user_system_message)):
            
            if author_role == "assistant":
                author_role = "ChatGPT"
            elif author_role == "user":
                author_role = "You"
            elif author_role == "system" and is_user_system_message:
                author_role = "Custom user info"

            data["messages"].append({"author": author_role, "text": content_parts[0]})
        
        current_node = node.get("parent")
    
    data["messages"].reverse()
    return data

def conversation_to_markdown(conversation: dict, filename: str):
    content = f"# {conversation['title']}\n\n"
    
    for message in conversation["messages"]:
        content += f"### **{message['author']}:**\n\n"
        content += f"{message['text']}\n\n"
    
    content_file = open(filename, "w", encoding="utf-8")
    content_file.write(content)
    content_file.close()