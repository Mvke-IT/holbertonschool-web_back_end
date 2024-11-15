import { expect } from "chai";
import kue from "kue";
import createPushNotificationsJobs from "./8-job";

const queue = kue.createQueue();
const list = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518952",
    message: "This is the code 5678 to verify your account",
  },
];

before(() => {
  queue.testMode.enter(true);
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe("test of queue", () => {
  it("display an error message if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("", queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("create two new jobs to the queue", () => {
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.eql({
      phoneNumber: "4153518952",
      message: "This is the code 5678 to verify your account",
    });
  });
});