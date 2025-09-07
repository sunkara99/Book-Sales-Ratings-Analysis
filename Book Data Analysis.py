# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv ("Books_Data_Clean.csv")


# %%
df.head()


# %%
df.describe()

# %%
df = df[df["Publishing Year"] > 1900]

# %%
df.isna().sum()


# %%
df.dropna(subset="Book Name", inplace= True)

# %%
df.duplicated().sum()

# %%
df.nunique()

# %%
plt.hist(df["Publishing Year"])
plt.xlabel("Publishing Year")
plt.ylabel("frequency")
plt.title("Distribution of publishing year")
plt.show()

# %%
df["genre"].value_counts().plot(kind = "bar")
plt.xlabel("genre")
plt.ylabel("number of books")
plt.title("Number of books in each genre")
plt.show()

# %%
df.groupby("Author")["Book_average_rating"].mean().sort_values(ascending = False)

# %%
sns.boxplot(x= "genre", y = "Book_ratings_count", data= df)
plt.xlabel("genre")
plt.ylabel("Book_ratings_count")
plt.title("Box plot of Book ratings Count for each genre")
plt.show()

# %%
plt.scatter(df["sale price"], df["units sold"])
plt.xlabel("sale price")
plt.ylabel("units sold")
plt.title("scatter Plot of sale Price vs Units Sold")
plt.show()

# %%
language_count = df["language_code"].value_counts()

# %%
plt.pie(language_count, labels=language_count.index, startangle= 90, autopct= "%1.1f%%")
plt.title("Language Distribution of Books")
plt.show()


# %%
df.columns

# %%
df.groupby("Publisher ")["publisher revenue"].sum()

# %%
df.groupby("Author_Rating")["Book_ratings_count"].mean()

# %%
df.groupby("language_code").size().sort_values(ascending=False)

# %%
df.groupby("Author_Rating")["Book_ratings_count"].mean()

# %%
plt.scatter(df["Book_average_rating"], df["Book_ratings_count"])
plt.xlabel("Book_average_rating")
plt.ylabel("Book_ratings_count")
plt.title("Scatter Plot of Book Average Rating Vs Book Ratings Count")
plt.show()

# %%
Total_gross_sales_by_author = df.groupby("Author")["gross sales"].sum()

# %%
Total_gross_sales_by_author.sort_values(ascending= False).head(10).plot(kind = "bar")
plt.xlabel("Author")
plt.ylabel("Total gross sales")
plt.show()

# %%
sns.boxplot(x= "Author_Rating", y = "units sold", data = df)
plt.xlabel("Author rating")
plt.ylabel("units sold")
plt.title("Box plot of unit sold for each Author rating")
plt.show()

# %%
df.groupby("Publishing Year")["units sold"].sum().plot(kind = "line", marker = "o")
plt.xlabel("Publishing Year")
plt.ylabel("Total unis sold")
plt.title("Total units sold over the years")
plt.show()


