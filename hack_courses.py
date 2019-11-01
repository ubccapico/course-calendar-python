import pandas as pd


def main():
    df = pd.read_csv("ubc_course_calendar_data.csv")

    print("Data fields:", df.columns.to_list())

    print("Total number of records:", len(df))

    print("Number of offerings per session:")
    print(df.groupby("SESSION_YEAR").size())


if __name__ == "__main__":
    main()
