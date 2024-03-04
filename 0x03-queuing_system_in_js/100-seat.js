/**
 * Basic seating app
 */
import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';
const express = require('express');

// Redis
const client = createClient();
client.get = promisify(client.get);

// Kue
const queue = createQueue();

// Express
const app = express();
const port = 1245;

let reservationEnabled = true;

/**
 * Set the available seats in Redis
 * @param {number} number The number to set for the available seats
 */
function reserveSeat (num) {
  client.set('available_seats', num);
}

/**
 * Returns the number of available seats
 */
async function getCurrentAvailableSeats () {
  const res = await client.get('available_seats');
  return res;
}

app.get('/available_seats', async function (req, res) {
  const currAv = await getCurrentAvailableSeats();

  res.json({ numberOfAvailableSeats: currAv });
});

app.get('/reserve_seat', function (req, res) {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat');

  job.on('complete', function (result) {
    console.log(`Seat reservation job ${job.id} completed`);
  }).on('failed', function (errorMessage) {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });

  job.save(function (err) {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });
});

app.get('/process', function (req, res) {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async function (job, done) {
    const nowAv = await getCurrentAvailableSeats() - 1;

    reserveSeat(nowAv);

    if (nowAv === 0) {
      reservationEnabled = false;
    }

    if (nowAv >= 0) {
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

reserveSeat(50);
app.listen(port, console.log('Server is listening at port', port));
