/**
 * Connects to a Redis server
 */
import { createClient, print } from 'redis';

const client = createClient();
client.on('error', err => console.log('Redis client not connected to the server:', err.message));
client.on('connect', () => console.log('Redis client connected to the server'));

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
function displaySchoolValue (schoolName) {
  client.get(schoolName, function (_, reply) {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
