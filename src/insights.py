from src import jobs


def get_unique_job_types(path):
    jobs_read = jobs.read(path)
    job_types = []
    for job in jobs_read:
        job_types.append(job["job_type"])
    myset = set(job_types)
    return list(myset)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
