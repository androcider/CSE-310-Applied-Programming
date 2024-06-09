using UnityEngine;
using UnityEngine.UI;
using TMPro; 
public class GameManager : MonoBehaviour
{
    public Button[] buttons;
    public Button resetButton;
    public TextMeshProUGUI winMessageText; // Reference to the UI Text element for win messages
    private string currentPlayer = "X";

    void Start()
    {
        if (buttons == null || buttons.Length != 9)
        {
            Debug.LogError("Buttons array is not initialized or does not have 9 elements.");
            return;
        }

        InitializeGame();

        // Add click event listener for the reset button
        resetButton.onClick.AddListener(ResetGame);
    }
    void InitializeGame()
    {
        for (int i = 0; i < buttons.Length; i++)
        {
            if (buttons[i] == null)
            {
                Debug.LogError($"Button at index {i} is not assigned.");
                continue;
            }

            TextMeshProUGUI buttonText = buttons[i].GetComponentInChildren<TextMeshProUGUI>(); // Use TextMeshProUGUI
            if (buttonText == null)
            {
                Debug.LogError($"TextMeshProUGUI component missing in button at index {i}.");
                continue;
            }

            buttonText.text = "";
            int index = i; // Local copy to avoid closure issue
            buttons[i].onClick.AddListener(() => OnButtonClick(index));
        }
    }

void OnButtonClick(int index)
{
    Debug.Log($"Button {index} clicked");

    TextMeshProUGUI buttonText = buttons[index].GetComponentInChildren<TextMeshProUGUI>(); // Use TextMeshProUGUI
    if (buttonText == null)
    {
        Debug.LogError($"TextMeshProUGUI component missing in button at index {index}.");
        return;
    }

    if (buttonText.text == "")
    {
        buttonText.text = currentPlayer;
        Debug.Log($"Setting button {index} text to {currentPlayer}");

        if (CheckWin())
        {
            Debug.Log($"Player {currentPlayer} wins!");
            // No need to reset here, let the player click the reset button
        }
        else if (CheckDraw())
        
        {
            Debug.Log("It's a draw!");
            // No need to reset here, let the player click the reset button

        }
        else
        {
            currentPlayer = currentPlayer == "X" ? "O" : "X";
            Debug.Log($"Current player is now {currentPlayer}");
        }
    }
}

    bool CheckWin()
    {
        string[,] board = new string[3, 3];
        for (int i = 0; i < buttons.Length; i++)
        {
            TextMeshProUGUI buttonText = buttons[i].GetComponentInChildren<TextMeshProUGUI>();
            int row = i / 3;
            int col = i % 3;
            board[row, col] = buttonText.text;
        }

        // Check rows
        for (int row = 0; row < 3; row++)
        {
            if (board[row, 0] != "" && board[row, 0] == board[row, 1] && board[row, 1] == board[row, 2])
            {
                DisplayWinMessage($"Player {currentPlayer} wins!");
                return true;
            }
        }

        // Check columns
        for (int col = 0; col < 3; col++)
        {
            if (board[0, col] != "" && board[0, col] == board[1, col] && board[1, col] == board[2, col])
            {
                DisplayWinMessage($"Player {currentPlayer} wins!");
                return true;
            }
        }

        // Check diagonals
        if (board[0, 0] != "" && board[0, 0] == board[1, 1] && board[1, 1] == board[2, 2])
        {
            DisplayWinMessage($"Player {currentPlayer} wins!");
            return true;
        }

        if (board[0, 2] != "" && board[0, 2] == board[1, 1] && board[1, 1] == board[2, 0])
        {
            DisplayWinMessage($"Player {currentPlayer} wins!");
            return true;
        }

        return false;
    }
bool CheckDraw()
{
    // Check if any button is still empty
    foreach (var button in buttons)
    {
        if (button.GetComponentInChildren<TextMeshProUGUI>().text == "")
            return false;
    }

    // If all buttons are filled and no win condition is met, it's a draw
    Debug.Log("Draw condition met!");
    DisplayWinMessage("It's a draw!");
    return true;
}
    void ResetGame()
    {
        currentPlayer = "X";
        for (int i = 0; i < buttons.Length; i++)
        {
            if (buttons[i] == null)
            {
                Debug.LogError($"Button at index {i} is not assigned.");
                continue;
            }

            TextMeshProUGUI buttonText = buttons[i].GetComponentInChildren<TextMeshProUGUI>(); 
            if (buttonText == null)
            {
                Debug.LogError($"TextMeshProUGUI component missing in button at index {i}.");
                continue;
            }

            buttonText.text = "";
        }

        // Clear the win message text
        winMessageText.text = "";
    }
        void DisplayWinMessage(string message)
    {
        winMessageText.text = message;
    }
}