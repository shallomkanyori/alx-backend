/**
 * Implement Node Redis client subscriber
 */
import { createClient } from 'redis';

const sub = createClient();
sub.on('error', err => console.log('Redis client not connected to the server:', err.message));
sub.on('connect', () => console.log('Redis client connected to the server'));

sub.on('message', function (channel, message) {
  if (channel === 'holberton school channel') {
    console.log(message);

    if (message === 'KILL_SERVER') {
      sub.unsubscribe();
      sub.quit();
    }
  }
});

sub.subscribe('holberton school channel');
