/**
 * Job processor
 */
import { createQueue } from 'kue';

const queue = createQueue();

/**
 * Logs the action of sending a notification
 * @param {string} phoneNumber The phone number to send the notification to
 * @param {string} message The message to send
 */
function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', function (job) {
  sendNotification(job.data.phoneNumber, job.data.message);
});
