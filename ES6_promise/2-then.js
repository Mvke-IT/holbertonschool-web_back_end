export default function handleResponseFromApi(promise) {
  eturn promise.then(() => (
    { status: 200, body: 'success' }))
    .catch(() => new Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}
