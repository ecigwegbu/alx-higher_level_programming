#include "lists.h"
#define BUFFSIZE 1024

int check_item(listint_t **head, int idx, int idx_mirror);
size_t build_array(listint_t **head, int *array);

/**
 * is_palindrome - check if a singly linked list is s palindrome
 * @head: address of the pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i, i_mirror, stop_at = 0;
	int array[BUFFSIZE];

	/* check if pointer is NULL or list is empty*/
	if (head == NULL || *head == NULL)
	{
	return (1);
	}

	/* build array and return the length len*/
	len = build_array(head, array);

	/* check each noode and it's mirror */
	stop_at = (len / 2) - 1;
	for (i = 0; i <= stop_at; i++)
	{
		i_mirror = len - (i + 1);

		/* compare i and i_mirror in one step --debug */
		if (array[i] != array[i_mirror])
			return (0); /* not a palindrome */
	}

	return (1);
}

/**
 * check_item - check item in a singly linked list against mirror position
 * @head: address of the pointer to the head of the linked list
 * @idx: index position, 0-based
 * @idx_mirror: mirror index position, 0-based
 * Return: 0 if not matched, 1 if matched
 */
int check_item(listint_t **head, int idx, int idx_mirror)
{
	listint_t *ptr = *head;
	int pos, n1, n2;

	for (pos = 0; pos < idx_mirror; pos++, ptr = ptr->next)
	{
		if (ptr == NULL)
		{
			perror("get_item");
			exit(EXIT_FAILURE);
		}

		if (pos == idx)
		{
			n1 = ptr->n;
		}
	}
	n2 = ptr->n;

	return (n1 == n2 ? 1 : 0);
}

/**
 * build_array - build array of elements and return the length len
 * @head: address of the pointer to the head of the linked list
 * @array: array of list elements
 * Return: length of list, 0 - based
 */
size_t build_array(listint_t **head, int *array)
{
	listint_t *ptr = *head;
	size_t pos = 0;

	while (ptr)  /* if you reach NULL that is the end of the list */
	{
		/* *array[pos] = ptr->n;  debug */
		array[pos] = ptr->n;
		ptr = ptr->next;
		pos++;
	}

	return (pos);
}
