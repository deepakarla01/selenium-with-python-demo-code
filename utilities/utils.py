import csv
import logging
import softest


class Utils(softest.TestCase):

    # Class-level logger initialization
    logger = None

    @staticmethod
    def custom_logger(logLevel=logging.DEBUG):
        if Utils.logger is None:  # Ensure logger is created only once
            # Create logger
            logger = logging.getLogger("DemoQABDDLogger")

            # Set logger level
            logger.setLevel(logLevel)

            # Create file handler and set the log level
            file_handler = logging.FileHandler("DemoQA_With_Logging_Fixture.log")
            file_handler.setLevel(logLevel)

            # Create formatter - how you want your logs to be formatted
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s - %(module)s"
            )

            # Add formatter to file handler
            file_handler.setFormatter(formatter)

            # Add file handler to logger
            logger.addHandler(file_handler)

            # Stream handler (used by pytest caplog) with filter
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            stream_handler.setFormatter(formatter)

            class GherkinOnlyFilter(logging.Filter):
                def filter(self, record):
                    # Only allow Gherkin steps to propagate to caplog/HTML report
                    return (
                        record.getMessage()
                        .strip()
                        .startswith(
                            (
                                "Given",
                                "When",
                                "Then",
                                "And",
                                "But",
                                "Feature",
                                "Scenario",
                            )
                        )
                    )

            stream_handler.addFilter(GherkinOnlyFilter())
            logger.addHandler(stream_handler)

            Utils.logger = logger  # Assign the logger to the class-level attribute

        Utils.logger.propagate = False  # Prevent propagation to root logger
        return Utils.logger

    @staticmethod
    def read_data_from_csv(filename):
        log = Utils.custom_logger()
        try:
            with open(filename, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                header = next(csv_reader)  # Skip the header row

                # Return single-column data as a list of strings, cleaning \xa0 from each ent
                if len(header) == 1:
                    return [row[0].replace("x\a0", "").strip() for row in csv_reader]

                # Return multi-column data as a list of tuples, cleaning \xa0 from each ent
                return [
                    tuple(row[i].replace("x\a0", "").strip() for i in range(len(row)))
                    for row in csv_reader
                ]
        except Exception as e:
            log.error("An unexpected error occurred in read_data_from_csv.", exc_info=e)
        finally:
            log.info("Completed execution of read_data_from_csv without exceptions.")

    @staticmethod
    def assert_text(self, expected_text, actual_text):
        log = Utils.custom_logger()
        try:
            assert expected_text in actual_text
            log.debug("assertion passed for, " + actual_text)
        except AssertionError:
            log.error("assertion failed for, " + actual_text)
        finally:
            log.info("Completed execution of assert_text without exceptions.")

    def check_expected_url(self, expected_url, actual_url):
        log = Utils.custom_logger()
        try:
            if expected_url in actual_url:
                log.info(
                    f"Expected URL: {expected_url} is in the actual url: {actual_url}"
                )
                return True
            else:
                log.error(
                    f"Expected URL: {expected_url} is not in the actual url: {actual_url}"
                )
                return False
        except Exception as e:
            log.error("An unexpected error occurred in check_expected_url: {e}")
