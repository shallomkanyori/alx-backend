/**
 * Job creation tests
 */
import createPushNotificationsJobs from './8-job.js';
import { createQueue } from 'kue';
import chai from 'chai';

const expect = chai.expect;
const queue = createQueue();

describe('createPushNotificationJobs', function () {
  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('should add a job to the queue', function () {
    const jobList = [{ phoneNumber: '0984327546', message: 'Test' }];
    createPushNotificationsJobs(jobList, queue);

    expect(queue.testMode.jobs.length).to.equal(1);

    const qJob = queue.testMode.jobs[0];
    expect(qJob.type).to.equal('push_notification_code_3');
    expect(qJob.data).to.deep.equal(jobList[0]);
  });

  it('should add two jobs to the queue', function () {
    const jobList = [{ phoneNumber: '0984327546', message: 'Test 0' },
      { phoneNumber: '0934123985', message: 'Test 1' }];
    createPushNotificationsJobs(jobList, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobList[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobList[1]);
  });

  it('should throw an error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('non list', queue)).to.throw(Error, 'Jobs is not an array');
  });
});
