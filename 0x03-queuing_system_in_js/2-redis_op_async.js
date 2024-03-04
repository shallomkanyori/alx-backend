/**
 * Connects to a Redis server
 */
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err.message));
client.on('connect', () => console.log('Redis client connected to the server'));

client.get = promisify(client.get);

/**
 * Sets in Redis the value for the a key
 * @param {string} schoolName The key to set a value for
 * @param {*} value The value to set for the key
 */
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Logs to the console the value for the key passed in
 * @param {string} schoolName The key to display the value for
 */
async function displaySchoolValue (schoolName) {
  const reply = await client.get(schoolName);
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
