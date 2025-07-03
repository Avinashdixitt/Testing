package jenkinsAssignment;

import static io.restassured.RestAssured.baseURI;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.json.simple.JSONObject;

public class assignment3Test {

    @BeforeClass
    public void setup() {
        baseURI = "http://localhost:3000";  // JSON Server base URL
    }

    @Test
    public void testGetAllEmployees() {
        given()
        .when()
        .get("/employees")
        .then()
        .statusCode(200)
        .log().body();  // Logs the full employee list
    }

    @Test
    public void testGetEmployeeById() {
        given()
        .when()
        .get("/employees/2")
        .then()
        .statusCode(200)
        .body("employee_name", equalTo("Garrett Winters"))
        .log().body();
    }

    @Test
    public void testCreateEmployee() {
        JSONObject request = new JSONObject();
        request.put("employee_name", "Avinash Dixit");
        request.put("employee_salary", 550000);
        request.put("employee_age", 26);
        request.put("profile_image", "");

        given()
            .header("Content-Type", "application/json")
            .body(request.toJSONString())
        .when()
            .post("/employees")
        .then()
            .statusCode(201)  // JSON Server returns 201 on creation
            .log().body();
    }

    @Test
    public void testUpdateEmployee() {
        JSONObject request = new JSONObject();
        request.put("employee_name", "Avinash Dixit Updated");
        request.put("employee_salary", 600000);
        request.put("employee_age", 27);
        request.put("profile_image", "");

        given()
            .header("Content-Type", "application/json")
            .body(request.toJSONString())
        .when()
            .put("/employees/3")  // Updating employee with ID = 1
        .then()
            .statusCode(200)
            .log().body();
    }

    @Test
    public void testDeleteEmployee() {
        given()
        .when()
        .delete("/employees/1")  // Deletes employee with ID = 1
        .then()
        .statusCode(200)
        .log().body();
    }
}
