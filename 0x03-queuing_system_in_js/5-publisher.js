/**
 * Implement Node Redis client publisher
 */
import { createClient } from 'redis';

const pub = createClient();
pub.on('error', err => console.log('Redis client not connected to the server:', err.message));
pub.on('connect', () => console.log('Redis client connected to the server'));

/**
 * Publishes a message
 * @param {string} message The message to publish
 * @param {number} time The time in ms to wait before publishing
 */
function publishMessage (message, time) {
  setTimeout(() => {
    console.log('About to send', message);
    pub.publish('holberton school channel', message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
