def calculate_machine_epsilon():
    """
    Calculate the machine epsilon, which is the smallest number that can be added to 1.0 to produce a distinct number greater than 1.0.
    """
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps /= 2.0
    return eps * 2.0
