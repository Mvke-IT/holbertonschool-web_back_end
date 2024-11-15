import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("connect", () => console.log("Redis client connected to the server"));

client.on("error", (err) => console.log("Redis Client Error", err));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client);
function displaySchoolValue(schoolName) {
  get(schoolName).then((res) => console.log(res));
}
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");