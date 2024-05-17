function handleResponseFromAPI(promise) {
    return promise.then(() => {
      try {
        const result = {
          status: 200,
          body: 'success',
        };
        console.log('Got a response from the API');  // Moved inside .then()
        return result; 
      } catch (error) {
        throw new Error('The fake API is not working currently');
      }
    })
      .catch(() => new Error('The fake API is not working currently')); 
  }
  