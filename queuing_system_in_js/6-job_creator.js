import kue from "kue";

const queue = kue.createQueue();

const jobData = { phoneNumber: "0679784423", message: "Here a texto" };

const job = queue.create("push_notification_code", jobData).save((err) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => console.log("Notification job completed"));
job.on("failure", () => console.log("Notification job failed"));