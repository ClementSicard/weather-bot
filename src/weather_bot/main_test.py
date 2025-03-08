"""Tests for the main function."""


def test_1() -> None:
    """Test that the main function does not raise an AssertionError."""
    from weather_bot.main import main

    main()

    assert True
