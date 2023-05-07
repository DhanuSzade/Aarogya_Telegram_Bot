#!/usr/bin/env python
# coding: utf-8

# In[1]:


import telegram.ext


# In[2]:


with open('token.txt','r') as f:
    TOKEN = f.read()


# In[9]:


print('Starting up Bot....')


def start_command(update, context):
    update.message.reply_text("Hello Welcome to Aarogya Bot !")
    
def help_command(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start -> Welcome Message 
    /help -> This Message
    /content -> Information About Homeopathy Doctors 
    /contact -> Information About Contact Details
    """)

def content_command(update, context):
    update.message.reply_text("  Homeopathy Doctor contact Number ")
    
def contact_command(update, context):
    update.message.reply_text(" Dr. Ashwin zade-07127751767, Dr.Gauri zade-7845129630 ")
    
def custom_response(update, context):
    update.message.reply_text('This is Custom Messgae')
    
    
def handle_response(text: str) -> str:
    if 'Hello' in text:
        return 'Hey there!'
    
    
    return 'Idk'

def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''
    
    
    print(f'User({update.message.chat.id}) says: "{text} in: {message_type}"')
    
    
    if message_type == 'group':
        if '@AarogyaBot' in text:
            new_text = text.replace('@AarogyaBot','').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)
        
    update.message.reply_text (response)
       
def error(update, context):
    print(f'Update{update} caused error: {context.error}')
    
    
    if __name__ =='__main__':
        updater = Updater(keys.token, use_context=True)
        dp = updater.dispatcher
        
        
        
        #commands
        dp.add_handler(CommandHandler('start', start_command))
        dp.add_handler(CommandHandler('help', help_command))
        dp.add_handler(CommandHandler('content', content_command))
        dp.add_handler(CommandHandler('contact', contact_command))
        
        
        # messages
        dp.add_handler(MessageHandler(Filters.text, handle_message))
        
        
        # Errors
        dp.add_error_handler(error)
        
        
        # Run Bot
        updater.start_polling(1,0)
        updater.idle()
        


# In[ ]:




