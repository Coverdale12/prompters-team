using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Telegram.Bot;
using Telegram.Bot.Exceptions;
using Telegram.Bot.Types;
public class MessengerTelegramNotifier
{
    // Настройка подключения к базе данных (замените на ваши значения)
    private readonly string _connectionString = "YOUR_CONNECTION_STRING";

    // Токен вашего Telegram бота
    private readonly string _telegramBotToken = "8019659864:AAEuXvOdgJPs2OCgrvhQdGglsMyHBmbPLNM";

    private readonly TelegramBotClient _telegramBotClient;


    public MessengerTelegramNotifier()
    {
        _telegramBotClient = new TelegramBotClient(_telegramBotToken);
    }


    public async Task Run()
    {
        try
        {
            // Периодически проверяйте базу данных
            while (true)
            {
                var newMessages = GetNewMessages();

                if (newMessages.Any())
                {
                    foreach (var message in newMessages)
                    {
                        await SendMessageToTelegram(message);
                    }
                }

                await Task.Delay(60000); // Проверяем каждые 60 секунд (измените, если нужно)
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка: {ex.Message}");
            Console.WriteLine($"Стек трейса: {ex.StackTrace}");

            // Важно: Обработайте исключения, чтобы программа не рухнула.
            // Например, логгируйте ошибки или отправляйте уведомление об ошибке в Telegram.
        }
    }

    private IQueryable<MessageData> GetNewMessages()
    {
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();

            // Запрос к базе данных для получения новых сообщений
            //  (замените на ваш SQL запрос)
            //  Важно:  Убедитесь, что поле "SentToTelegram" есть в таблице
            string sqlQuery = @"
                SELECT *
                FROM Messages
                WHERE SentToTelegram = 0
                OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;  -- Получаем только 10 новых
            ";

            using (var command = new SqlCommand(sqlQuery, connection))
            {
                var reader = command.ExecuteReader();
                return reader.Cast<MessageData>().AsQueryable();
            }
        }
    }


    private async Task SendMessageToTelegram(MessageData message)
    {
        try
        {
            var chatId = message.RecipientId; // Получите ID чата из message
            var messageText = message.Text;

            // Отправка сообщения в Telegram
            await _telegramBotClient.SendTextMessageAsync(chatId, messageText);

            // Обновление статуса в базе данных
            UpdateMessageStatus(message.MessageId);

        }
        catch (Exception ex)
        {
            Console.WriteLine($"Ошибка отправки сообщения в Telegram: {ex.Message}");
            Console.WriteLine($"Стек трейса: {ex.StackTrace}");
            // Обработка ошибок (например, запись в лог или уведомление)
            // важно не терять данные
        }
    }

    //Метод обновления статуса сообщения в базе данных
    private void UpdateMessageStatus(int messageId)
    {
        // SQL запрос для обновления статуса
        // Измените на вашу таблицу и поле
        using (var connection = new SqlConnection(_connectionString))
        {
            connection.Open();
            var command = new SqlCommand("UPDATE Messages SET SentToTelegram = 1 WHERE MessageId = @MessageId", connection);
            command.Parameters.AddWithValue("@MessageId", messageId);
            command.ExecuteNonQuery();
        }
    }


    // Класс для данных сообщения (подстройте под вашу базу данных!)

 
public class MessageData
    {
        public int MessageId { get; set; }
        public string Text { get; set; }
        public int RecipientId { get; set; } // Идентификатор чата в Telegram
        public int SentToTelegram { get; set; } // Флаг отправлено ли сообщение в Telegram
    }

    public static void Main(string[] args)
    {
        var notifier = new MessengerTelegramNotifier();
        Task.Run(async () => await notifier.Run());
        Console.ReadLine();
    }
}