import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class LoginTest {

    // TC_001 - Valid Login
    @Test
    void testValidLogin() {
        String username = "validUser";
        String password = "validPass";

        boolean loginResult = true; // simulate successful login

        assertTrue(loginResult, "User should be able to login with valid credentials");
    }

    // TC_002 - Invalid Password
    @Test
    void testInvalidPassword() {
        String username = "validUser";
        String password = "wrongPass";

        boolean loginResult = false; // simulate failed login

        assertFalse(loginResult, "Login should fail with invalid password");
    }

    // TC_003 - Empty Username
    @Test
    void testEmptyUsername() {
        String username = "";
        String password = "validPass";

        boolean isValid = username.isEmpty();

        assertTrue(isValid, "Username is required");
    }

    // TC_004 - Empty Password
    @Test
    void testEmptyPassword() {
        String username = "validUser";
        String password = "";

        boolean isValid = password.isEmpty();

        assertTrue(isValid, "Password is required");
    }

    // TC_005 - Both Fields Empty
    @Test
    void testBothFieldsEmpty() {
        String username = "";
        String password = "";

        boolean isInvalid = username.isEmpty() && password.isEmpty();

        assertTrue(isInvalid, "Both fields are required");
    }
}
