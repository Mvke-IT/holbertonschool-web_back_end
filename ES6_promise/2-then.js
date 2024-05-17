function handleResponseFromAPI(promise) {
  return promise.then(() => {
    try {
      return {
        status: 200,
        body: 'success',
      };
    } catch (error) {
      throw new Error('The fake API is not working currently');
    }
  })
    .catch(() => new Error('The fake API is not working currently'))
    .finally(() => console.log('Got a response from the API'));
}

export default handleResponseFromAPI;
