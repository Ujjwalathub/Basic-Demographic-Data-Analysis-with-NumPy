import numpy as np

# Sample data for 15 people
names = np.array([
    'Alice', 'Bob', 'Charlie', 'Diana', 'Ethan',
    'Fiona', 'George', 'Hannah', 'Ian', 'Julia',
    'Kevin', 'Laura', 'Mike', 'Nina', 'Oscar'
])

ages = np.array([25, 32, 45, 29, 36, 28, 50, 22, 41, 30, 33, 27, 38, 26, 40])

genders = np.array([
    'Female', 'Male', 'Male', 'Female', 'Male',
    'Female', 'Male', 'Female', 'Male', 'Female',
    'Male', 'Female', 'Male', 'Female', 'Male'
])

occupations = np.array([
    'Engineer', 'Doctor', 'Teacher', 'Designer', 'Engineer',
    'Doctor', 'Artist', 'Student', 'Manager', 'Engineer',
    'Lawyer', 'Teacher', 'Scientist', 'Nurse', 'Architect'
])

education_levels = np.array([
    'Master', 'PhD', 'Bachelor', 'Bachelor', 'Master',
    'PhD', 'High School', 'Bachelor', 'Master', 'Bachelor',
    'PhD', 'Bachelor', 'PhD', 'Bachelor', 'Master'
])

nationalities = np.array([
    'USA', 'Canada', 'UK', 'USA', 'Germany',
    'Canada', 'France', 'India', 'Germany', 'USA',
    'UK', 'France', 'USA', 'India', 'Canada'
])

# Convert gender to numeric: Male = 1, Female = 0
gender_numeric = np.where(genders == 'Male', 1, 0)

# Basic stats
mean_age = np.mean(ages)
median_age = np.median(ages)
max_age = np.max(ages)
min_age = np.min(ages)

# Gender distribution
num_males = np.sum(gender_numeric)
num_females = len(gender_numeric) - num_males

# Occupation frequency
unique_jobs, job_counts = np.unique(occupations, return_counts=True)

# Education distribution
unique_edu, edu_counts = np.unique(education_levels, return_counts=True)

# Nationality distribution
unique_nat, nat_counts = np.unique(nationalities, return_counts=True)

# Output
print("=== Basic Statistics ===")
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Max Age: {max_age}")
print(f"Min Age: {min_age}")

print("\n=== Gender Distribution ===")
print(f"Males: {num_males}")
print(f"Females: {num_females}")

print("\n=== Occupation Frequency ===")
for job, count in zip(unique_jobs, job_counts):
    print(f"{job}: {count}")

print("\n=== Education Level Distribution ===")
for edu, count in zip(unique_edu, edu_counts):
    print(f"{edu}: {count}")

print("\n=== Nationality Distribution ===")
for nat, count in zip(unique_nat, nat_counts):
    print(f"{nat}: {count}")
