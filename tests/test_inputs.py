"""Tests for CLI input functions."""

import pytest
from unittest.mock import patch

from todo.cli.inputs import get_task_content, get_task_id, get_menu_choice, confirm_action
from todo.exceptions import InvalidInputError


class TestGetTaskContent:
    """Tests for get_task_content function."""

    @patch("todo.cli.inputs.input")
    def test_valid_content(self, mock_input):
        """Test that valid content is returned."""
        mock_input.return_value = "Buy groceries"
        result = get_task_content()
        assert result == "Buy groceries"
        mock_input.assert_called_once()

    @patch("todo.cli.inputs.input")
    def test_content_strips_whitespace(self, mock_input):
        """Test that content is stripped of whitespace."""
        mock_input.return_value = "  Buy groceries  "
        result = get_task_content()
        assert result == "Buy groceries"

    @patch("todo.cli.inputs.input")
    def test_empty_input_reprompts(self, mock_input):
        """Test that empty input causes reprompt."""
        mock_input.side_effect = ["", "", "Valid task"]
        result = get_task_content()
        assert result == "Valid task"
        assert mock_input.call_count == 3

    @patch("todo.cli.inputs.input")
    def test_too_long_input_reprompts(self, mock_input):
        """Test that too long input causes reprompt."""
        long_content = "x" * 501
        mock_input.side_effect = [long_content, "Valid task"]
        result = get_task_content()
        assert result == "Valid task"
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_custom_prompt(self, mock_input):
        """Test that custom prompt is used."""
        mock_input.return_value = "Test task"
        get_task_content("Enter your task: ")
        mock_input.assert_called_with("Enter your task: ")


class TestGetTaskId:
    """Tests for get_task_id function."""

    @patch("todo.cli.inputs.input")
    def test_valid_id(self, mock_input):
        """Test that valid ID is returned."""
        mock_input.return_value = "5"
        result = get_task_id()
        assert result == 5

    @patch("todo.cli.inputs.input")
    def test_zero_id_reprompts(self, mock_input):
        """Test that zero ID causes reprompt."""
        mock_input.side_effect = ["0", "5"]
        result = get_task_id()
        assert result == 5
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_negative_id_reprompts(self, mock_input):
        """Test that negative ID causes reprompt."""
        mock_input.side_effect = ["-1", "5"]
        result = get_task_id()
        assert result == 5
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_non_numeric_input_reprompts(self, mock_input):
        """Test that non-numeric input causes reprompt."""
        mock_input.side_effect = ["abc", "5"]
        result = get_task_id()
        assert result == 5
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_empty_input_reprompts(self, mock_input):
        """Test that empty input causes reprompt."""
        mock_input.side_effect = ["", "5"]
        result = get_task_id()
        assert result == 5
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_custom_prompt(self, mock_input):
        """Test that custom prompt is used."""
        mock_input.return_value = "5"
        get_task_id("Enter task ID: ")
        mock_input.assert_called_with("Enter task ID: ")


class TestGetMenuChoice:
    """Tests for get_menu_choice function."""

    @patch("todo.cli.inputs.input")
    def test_valid_choice(self, mock_input):
        """Test that valid choice is returned."""
        mock_input.return_value = "3"
        result = get_menu_choice()
        assert result == 3

    @patch("todo.cli.inputs.input")
    def test_valid_choice_boundary_min(self, mock_input):
        """Test that minimum boundary choice works."""
        mock_input.return_value = "1"
        result = get_menu_choice((1, 7))
        assert result == 1

    @patch("todo.cli.inputs.input")
    def test_valid_choice_boundary_max(self, mock_input):
        """Test that maximum boundary choice works."""
        mock_input.return_value = "7"
        result = get_menu_choice((1, 7))
        assert result == 7

    @patch("todo.cli.inputs.input")
    def test_out_of_range_reprompts(self, mock_input):
        """Test that out of range choice causes reprompt."""
        mock_input.side_effect = ["0", "8", "3"]
        result = get_menu_choice()
        assert result == 3
        assert mock_input.call_count == 3

    @patch("todo.cli.inputs.input")
    def test_non_numeric_input_reprompts(self, mock_input):
        """Test that non-numeric input causes reprompt."""
        mock_input.side_effect = ["abc", "3"]
        result = get_menu_choice()
        assert result == 3
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_empty_input_reprompts(self, mock_input):
        """Test that empty input causes reprompt."""
        mock_input.side_effect = ["", "3"]
        result = get_menu_choice()
        assert result == 3
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_custom_prompt(self, mock_input):
        """Test that custom prompt is used."""
        mock_input.return_value = "3"
        get_menu_choice(prompt="Choose: ")
        mock_input.assert_called_with("Choose: ")

    @patch("todo.cli.inputs.input")
    def test_custom_range(self, mock_input):
        """Test that custom range is respected."""
        mock_input.side_effect = ["0", "1"]
        result = get_menu_choice((1, 3))
        assert result == 1


class TestConfirmAction:
    """Tests for confirm_action function."""

    @patch("todo.cli.inputs.input")
    def test_confirm_yes(self, mock_input):
        """Test that 'y' returns True."""
        mock_input.return_value = "y"
        result = confirm_action()
        assert result is True

    @patch("todo.cli.inputs.input")
    def test_confirm_yes_uppercase(self, mock_input):
        """Test that 'Y' returns True."""
        mock_input.return_value = "Y"
        result = confirm_action()
        assert result is True

    @patch("todo.cli.inputs.input")
    def test_confirm_yes_full_word(self, mock_input):
        """Test that 'yes' returns True."""
        mock_input.return_value = "yes"
        result = confirm_action()
        assert result is True

    @patch("todo.cli.inputs.input")
    def test_confirm_no(self, mock_input):
        """Test that 'n' returns False."""
        mock_input.return_value = "n"
        result = confirm_action()
        assert result is False

    @patch("todo.cli.inputs.input")
    def test_confirm_no_uppercase(self, mock_input):
        """Test that 'N' returns False."""
        mock_input.return_value = "N"
        result = confirm_action()
        assert result is False

    @patch("todo.cli.inputs.input")
    def test_confirm_no_full_word(self, mock_input):
        """Test that 'no' returns False."""
        mock_input.return_value = "no"
        result = confirm_action()
        assert result is False

    @patch("todo.cli.inputs.input")
    def test_invalid_input_reprompts(self, mock_input):
        """Test that invalid input causes reprompt."""
        mock_input.side_effect = ["maybe", "y"]
        result = confirm_action()
        assert result is True
        assert mock_input.call_count == 2

    @patch("todo.cli.inputs.input")
    def test_custom_prompt(self, mock_input):
        """Test that custom prompt is used."""
        mock_input.return_value = "y"
        confirm_action("Proceed? ")
        mock_input.assert_called_with("Proceed? ")
