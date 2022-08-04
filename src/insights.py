from src import jobs


def get_unique_job_types(path):
    jobs_read = jobs.read(path)
    job_types = []
    for job in jobs_read:
        job_types.append(job["job_type"])
    myset = set(job_types)
    return list(myset)


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    jobs_read = jobs.read(path)
    industries_list = []
    for job in jobs_read:
        if len(job["industry"]) > 0:
            industries_list.append(job["industry"])
    myset = set(industries_list)
    mylist = list(myset)
    return mylist


def filter_by_industry(jobs, industry):
    industries_list = []
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    jobs_read = jobs.read(path)
    salary = 0
    for job in jobs_read:
        try:
            if int(job["max_salary"]) > salary:
                salary = int(job["max_salary"])
        except ValueError:
            pass
    return salary


# https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed


def get_min_salary(path):
    jobs_read = jobs.read(path)
    salary = get_max_salary(path)
    for job in jobs_read:
        try:
            if int(job["min_salary"]) < salary:
                salary = int(job["min_salary"])
        except ValueError:
            pass
    return salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if type(salary) != int:
        raise ValueError
    return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    job_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                job_list.append(job)
        except ValueError:
            continue
    return job_list
