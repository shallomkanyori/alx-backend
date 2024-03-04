/**
 * Creates push notification code jobs from an array of objects
 * @param {object[]} jobs The array of objects with job data
 * @param {kue.Queue} queue The queue
 */
export default function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobObj of jobs) {
    const job = queue.create('push_notification_code_3', jobObj);

    job.on('complete', function (result) {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', function (errorMessage) {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    }).on('progress', function (progress, data) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    job.save(function (err) {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  }
}
