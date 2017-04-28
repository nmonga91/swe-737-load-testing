package yelp

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._
import org.asynchttpclient.oauth._

class TestYelpApi extends Simulation {
  val consumer_key = ""
  val consumer_secret = ""
  val token = ""
  val token_secret = ""
  val nonce = "omgthisissorandom"

  val consumer:ConsumerKey = new ConsumerKey(consumer_key, consumer_secret)
  val user = new RequestToken(token, token_secret)
  val calc = new OAuthSignatureCalculator(consumer, user)
  

  // val scn = scenario("My scenario").repeat(10000) {
  //   exec(
  //     http("Test Search San Francisco")
  //       .get("https://api.yelp.com/v2/search/?location=San Francisco, CA")
  //       .signatureCalc(calc)
  //       .check(status.is(200))
  //   )
  // }

  // setUp(scn.users(200).ramp(100))
}