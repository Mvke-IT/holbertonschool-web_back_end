import { createClient, print } from "redis";

const client = createClient();

client.on("connect", () => console.log("Redis client connected to the server"));

client.on("error", (err) => console.log("Redis Client Error", err));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, print);
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");