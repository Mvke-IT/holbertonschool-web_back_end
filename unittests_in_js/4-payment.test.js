const sinon = require("sinon");
const expect = require("chai").expect;
const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");

describe("sendPaymentRequestToApi", function () {
  it("should call Utils.calculateNumber with the correct arguments", function () {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const spyConsole = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(spyConsole.calledWith("The total is: 10")).to.be.true;

    stub.restore();
    spyConsole.restore();
  });
});