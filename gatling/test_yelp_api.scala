package basic

import com.excilys.ebi.gatling.core.Predef._
import com.excilys.ebi.gatling.http.Predef._
import com.excilys.ebi.gatling.jdbc.Predef._
import akka.util.duration._
import bootstrap._
import assertions._

class ExampleSimulation extends Simulation {
  val scn = scenario("My scenario").repeat(10000) {
    exec(
      http("My Page")
        .get("http://localhost:8080/test-webapp")
        .check(status.is(200))
    )
  }

  setUp(scn.users(200).ramp(100))
}