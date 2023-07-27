import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# # Create an instance of the bot
# bot = telebot.TeleBot('YOUR_BOT_TOKEN')



TOKEN="6076848296:AAEUzGB4-ZMoZSnkrYi6XCU"

bot = telebot.TeleBot(TOKEN, parse_mode=None) 



# Handle the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    # Create an inline keyboard with a single button
    keyboard = InlineKeyboardMarkup()
#     button = InlineKeyboardButton("Click me", callback_data='button_clicked')
    keyboard.row(InlineKeyboardButton("File Complaint", callback_data='file_omplaint'),InlineKeyboardButton("Track Complaint", callback_data='track_complaint'))

    # Send a message with the inline keyboard
    bot.send_message(message.chat.id, 'Choose the complaint type :', reply_markup=keyboard)

# Handle file_omplaint button clicks
@bot.callback_query_handler(func=lambda call: call.data == 'file_omplaint')
def handle_file_omplaint(call):
    # Answer the callback query
    bot.answer_callback_query(call.id, text='file_omplaint')

    # Create another inline keyboard with a new button
    file_omplaint = InlineKeyboardMarkup(row_width=1)
    Banks = InlineKeyboardButton("Banks", url='https://www.rbi.org.in/Scripts/ComplaintBank.aspx')
    NBFCs = InlineKeyboardButton("NBFCs", url='https://www.rbi.org.in/Scripts/ComplaintNBFC.aspx')
    PPI = InlineKeyboardButton("Prepaid Payment Instruments (PPI)", url='https://www.rbi.org.in/Scripts/ComplaintPPI.aspx')
    anybanks = InlineKeyboardButton("Any (banks , NBFCs,System Participants)", callback_data='anybanks')
    file_omplaint.row(Banks,)
    file_omplaint.row(NBFCs)
    file_omplaint.row(PPI)
    file_omplaint.row(anybanks)

    # Edit the message to display the new inline keyboard
#     bot.send_message(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Button clicked!',
#                           reply_markup=another_keyboard)

    bot.send_message(call.message.chat.id, 'Which specific Regulated Entity do you need to complaint against ? ', reply_markup=file_omplaint)

                            
# Handle another anybanks click
@bot.callback_query_handler(func=lambda call: call.data == 'anybanks')
def handle_anybanks_button_click(call):
    # Answer the callback query
    bot.answer_callback_query(call.id, text='anybanks')
    
    # Create another inline keyboard with a new button
    anybanks = InlineKeyboardMarkup(row_width=1)
    Individual = InlineKeyboardButton("Individual",callback_data='Individual')
    Trust = InlineKeyboardButton("Trust", callback_data='Trust')
    Government = InlineKeyboardButton("Trust", callback_data='Government')
    senior_citizen = InlineKeyboardButton("Senior Citizen", callback_data='senior_citizen')
    
#     anybanks.row(Individual,Trust,Government,senior_citizen)
    
    anybanks.row(Individual,)
    anybanks.row(Trust)
    anybanks.row(Government)
    anybanks.row(senior_citizen)
                                 
    bot.send_message(call.message.chat.id, 'Select Complainant Category ? ', reply_markup=anybanks)
                                 
                                 
                           
# Handle Individual buuton click
@bot.callback_query_handler(func=lambda call: call.data == 'Individual')
def handle_Individual_button_click(call):
    # Answer the callback query
    bot.answer_callback_query(call.id, text='Individual')
    
    # Create another inline keyboard with a new button
    Individual = InlineKeyboardMarkup()
    yes = InlineKeyboardButton("Yes to that",callback_data='yes')
    no = InlineKeyboardButton("Nah", callback_data='no')

    Individual.row(yes,no)
    
    
# #     Edit the message to display the new inline keyboard
#     bot.send_message(call.message.chat.id, text='Individual', reply_markup=Individual)  -- this will going to get the click button
    bot.send_message(call.message.chat.id, "Is your complaint sub-judice/under arbitration/alrady dealt with on merits by a Court/Tributional/Authority ?" , reply_markup=Individual)
                                

# def handle_Individual_button_click(call):
#     # Determine which button was clicked
#     if call.data == 'yes':
#         # Answer the callback query and send a response message for Button 1
#         bot.answer_callback_query(call.id, text='Yes to that')
#     elif call.data == 'no':
#         # Answer the callback query and send a response message for Button 2
#         bot.answer_callback_query(call.id, text='No ')

#     # Remove the inline keyboard
#     bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
#                                   reply_markup=None)

#     # Send a "Thank you" message
#     bot.send_message(call.message.chat.id, 'Thank you!')
    
    
@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def handle_button_click(call):
    # Answer the callback query
    bot.answer_callback_query(call.id, text='Yes to that')

    # Remove the inline keyboard
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=None)

    # Send a "Thank you" message
    bot.send_message(call.message.chat.id, 'Thank you for clicking the Yes to that button!')

    
    
@bot.callback_query_handler(func=lambda call: call.data == 'no')
def handle_button_click(call):
    # Answer the callback query
    bot.answer_callback_query(call.id, text='No')

    # Remove the inline keyboard
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  reply_markup=None)

    # Send a "Thank you" message
    bot.send_message(call.message.chat.id, 'Thank you !')


    
# Start the bot
bot.polling()
