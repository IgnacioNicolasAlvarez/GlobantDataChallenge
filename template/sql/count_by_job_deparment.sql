SELECT
    d.deparment AS department,
    j.job AS job,
    COALESCE(COUNT(*), 0) AS employee_count,
    CASE
        WHEN EXTRACT(
            MONTH
            FROM
                h.datetime
        ) BETWEEN 1
        AND 3 THEN 'Q1'
        WHEN EXTRACT(
            MONTH
            FROM
                h.datetime
        ) BETWEEN 4
        AND 6 THEN 'Q2'
        WHEN EXTRACT(
            MONTH
            FROM
                h.datetime
        ) BETWEEN 7
        AND 9 THEN 'Q3'
        ELSE 'Q4'
    END AS hire_quarter
FROM
    hired_employee h
    INNER JOIN job j ON h.job_id = j.job_id
    INNER JOIN department d ON h.department_id = d.department_id
WHERE
    EXTRACT(
        YEAR
        FROM
            h.datetime
    ) = 2021
GROUP BY
    j.job,
    d.deparment,
    hire_quarter
ORDER BY
    d.deparment,
    j.job ASC;