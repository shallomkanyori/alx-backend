/**
 * Job creator
 */
import { createQueue } from 'kue';

const queue = createQueue();

const jobObj = {
  phoneNumber: '0712309854',
  message: 'Test message'
};

const job = queue.create('push_notification_code', jobObj).save(function (err) {
  if (!err) {
    console.log('Notification job created:', job.id);
  }
});

job.on('complete', function (result) {
  console.log('Notification job completed');
}).on('failed', function (errorMessage) {
  console.log('Notification job failed');
});
