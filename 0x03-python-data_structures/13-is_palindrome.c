#include "lists.h"
#define BUFFSIZE 256

int check_item(listint_t **head, int idx, int idx_mirror);
size_t build_array(listint_t **head, int **ap);
long comp_lhs_rhs_totals(int *arr, size_t len);
void raise_error(void);

/**
 * is_palindrome - check if a singly linked list is s palindrome
 * @head: address of the pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	size_t len, i, i_mirror, stop_at;
	int *array = NULL;

	/* check if pointer is NULL or list is empty*/
	if (head == NULL || *head == NULL)
	{
	return (1);
	}

	/* build array and return the length len*/
	len = build_array(head, &array);

	/* compare totals for not a palindrome case */
	if (comp_lhs_rhs_totals(array, len))
	{
		free(array);
		return (0);
	}

	/* check each noode and it's mirror */
	stop_at = (len / 2) - 1;
	for (i = 0; i <= stop_at; i++)
	{
		i_mirror = len - (i + 1);

		/* compare i and i_mirror */
		if (array[i] != array[i_mirror])
		{
			free(array);
			return (0); /* not a palindrome */
		}
	}

	free(array);
	return (1);
}

/**
 * build_array - build array of elements and return the length len
 * @head: address of the pointer to the head of the linked list
 * @ap: pointer to array of list elements
 * Return: length of list, 0 - based
 */
size_t build_array(listint_t **head, int **ap)
{
	listint_t *ptr = *head;
	size_t i, pos = 0, buffsz = BUFFSIZE;

	/* allocate memory to array */
	*ap = malloc(sizeof(int) * buffsz);
	if (*ap == NULL)
		raise_error();
	/* init aray */
	for (i = 0; i < buffsz - 1; i++)
	{
		(*ap)[i] = 0;
	}

	while (ptr)  /* if you reach NULL that is the end of the list */
	{
		/* check if we are running out of space, if so realloc */
		if (pos == (buffsz - 1))
		{
			buffsz += (BUFFSIZE / 2);
			*ap = realloc(*ap, sizeof(int) * (buffsz));
			if (*ap == NULL)
				raise_error();
		}
		(*ap)[pos] = ptr->n;
		ptr = ptr->next;
		pos++;
	}

	*ap = realloc(*ap, sizeof(int) * pos);
	if (*ap == NULL)
		raise_error();
	return (pos);
}


/**
 * raise_error - raise a perror
 */
void raise_error(void)
{
	perror("build_array");
	exit(EXIT_FAILURE);
}

/**
 * comp_lhs_rhs_totals - compare totals of left and right hand sides
 * @arr: array of values
 * @len: length of array of values, 0 based
 * Return: 0 if equal, anything else if otherwise
 */
long comp_lhs_rhs_totals(int *arr, size_t len)
{
	size_t i, stop_at, i_mirror;
	long lh_tot = 0, rh_tot = 0;

	stop_at = (len / 2 - 1);
	i_mirror = len - (stop_at + 1);


	for (i = 0; i <= stop_at; i++)
		lh_tot += arr[i];

	for (i = i_mirror; i < len; i++)
		rh_tot += arr[i];

	return (lh_tot - rh_tot);
}
