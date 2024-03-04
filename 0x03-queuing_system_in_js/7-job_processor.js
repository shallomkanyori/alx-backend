/**
 * Job processor
 */
import { createQueue } from 'kue';

const queue = createQueue();

const blacklist = ['4153518780', '4153518781'];

/**
 * Processes a push_notification_code_2 job
 * @param {string} phoneNumber The phone number to send the notification to
 * @param {string} message The message to send
 * @param {kue.Job} job The job to process
 * @param {function} done The function to call to signify the job is done
 */
function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code_2', 2, function (job, done) {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
