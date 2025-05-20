import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Utils:
    def __init__(self, choice):
        self.choice = choice
        # Load all datasets and store as instance variables
        self.togo_df = pd.read_csv("../src/data/togo.csv", parse_dates=["Timestamp"]).set_index("Timestamp")
        self.sierraleone_df = pd.read_csv("../src/data/sierraleone_clean.csv", parse_dates=["Timestamp"]).set_index("Timestamp")
        self.benin_df = pd.read_csv("../src/data/benin-malanville_clean.csv", parse_dates=["Timestamp"]).set_index("Timestamp")

    def load_data(self):
        if self.choice == "Benin-malanville":
            return self.benin_df
        elif self.choice == "Sierraleone":
            return self.sierraleone_df
        elif self.choice == "Togo":
            return self.togo_df
        else:
            return None

    def show_summary(self, df):
        return df.describe()

    def show_corr(self, df):
        corr = df.corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("Correlation Heatmap")
        return fig

    def show_GHI(self, df):
        fig, ax = plt.subplots(figsize=(10, 6))
        df["GHI"].plot(ax=ax)
        ax.set_title("Global Horizontal Irradiance (GHI)")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("GHI (W/m²)")
        return fig

    def show_DNI(self, df):
        fig, ax = plt.subplots(figsize=(10, 6))
        df["DNI"].plot(ax=ax)
        ax.set_title("Direct Normal Irradiance (DNI)")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("DNI (W/m²)")
        return fig

    def show_DHI(self, df):
        fig, ax = plt.subplots(figsize=(10, 6))
        df["DHI"].plot(ax=ax)
        ax.set_title("Diffuse Horizontal Irradiance (DHI)")
        ax.set_xlabel("Timestamp")
        ax.set_ylabel("DHI (W/m²)")
        return fig

    def show_comparison(self):
        # Combine GHI from all three countries
        togo_ghi = self.togo_df[["GHI"]].copy()
        togo_ghi["country"] = "Togo"

        sierra_ghi = self.sierraleone_df[["GHI"]].copy()
        sierra_ghi["country"] = "Sierra Leone"

        benin_ghi = self.benin_df[["GHI"]].copy()
        benin_ghi["country"] = "Benin"

        combined_df = pd.concat([togo_ghi, sierra_ghi, benin_ghi])

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x="country", y="GHI", data=combined_df, ax=ax, palette="Set2")
        ax.set_title("Boxplot of GHI for All Countries")
        return fig
