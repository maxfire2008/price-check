import centre_com_seagate_firecuda_hdd_4tb
import centre_com_seagate_firecuda_hdd_8tb
import scorptec_seagate_firecuda_hdd_4tb
import scorptec_seagate_firecuda_hdd_8tb
import price_check_check

checks = [
    # centre_com_seagate_firecuda_hdd_4tb.price_check, NO LONGER AVAILABLE
    centre_com_seagate_firecuda_hdd_8tb.price_check,
    scorptec_seagate_firecuda_hdd_4tb.price_check,
    scorptec_seagate_firecuda_hdd_8tb.price_check,
    price_check_check.price_check_check,
]


def main():
    exit_code = 0
    for check in checks:
        print("Running check:", check.__module__ + "." + check.__name__)
        result = check()
        if result:
            print(
                "==========CHECK INFORMATION==========\n" +
                check.__module__ +
                "." +
                check.__name__ +
                ": " +
                result +
                "\n====================================="
            )
            exit_code = 1
        else:
            print("Check:", check.__module__ + "." +
                  check.__name__, "didn't return anything\n")
    return exit_code


if __name__ == "__main__":
    """
    Supply the following environment variables:
    EMAIL_FROM, EMAIL_TO, EMAIL_PASSWORD, EMAIL_HOST, EMAIL_PORT
    """
    quit(main())
