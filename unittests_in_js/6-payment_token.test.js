const expect = require("chai").expect;
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", function () {
  it("should return a resolved promise with a token when success is true", function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.eql({ data: "Successful response from the API" });
        done();
      })
      .catch(done);
  });
});