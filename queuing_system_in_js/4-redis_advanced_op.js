import { createClient, print } from "redis";

const client = createClient();

client.on("connect", () => console.log("Redis client connected to the server"));

client.on("error", (err) => console.log("Redis Client Error", err));

const cities = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.keys(cities).forEach((city) => {
  client.hset("HolbertonSchools", city, cities[city], print);
});

client.hgetall("HolbertonSchools", (err, object) => {
  console.log(object);
});