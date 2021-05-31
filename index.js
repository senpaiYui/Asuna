const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '-';

client.once('ready', () => {
    console.log('Senpai is online!');
});

client.on('message', message =>{
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'ping'){
        message.channel.send('pong!');
    } else if (command == 'ping'){
        message.channel.send('pong');
    }
});



client.login('ODM2OTc5ODgxNDk3MDY3NTMx.YIl4Qg.7w3HezVU6gT8oL7_UEC9h7nrLqA')