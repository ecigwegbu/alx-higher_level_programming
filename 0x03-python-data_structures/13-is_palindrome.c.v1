#include "lists.h"

int check_item(listint_t **head, int idx, int idx_mirror);
int get_item(listint_t **head, int idx);
int get_len(listint_t **head);

/**
 * is_palindrome - check if a singly linked list is s palindrome
 * @head: address of the pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i, i_mirror, stop_at = 0;

	/* check if pointer is NULL or list is empty*/
	if (head == NULL || *head == NULL)
	{
	return (1);
	}

	/* determine list length : len*/
	len = get_len(head);

	/* check each noode and it's mirror */
	stop_at = (len / 2) - 1;
	for (i = 0; i <= stop_at; i++)
	{
		i_mirror = len - (i + 1);
		/*if (get_item(head, i) != get_item(head, i_mirror)) */

		/* compare i and i_mirror in one step --debug */
		if (!check_item(head, i, i_mirror))
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
 * get_item - get item in a singly linked list at a given index position
 * @head: address of the pointer to the head of the linked list
 * @idx: index position, 0-based
 * Return: value at given index
 */
int get_item(listint_t **head, int idx)
{
	listint_t *ptr = *head;
	int pos;

	for (pos = 0; pos < idx; pos++)
	{
		if (ptr == NULL)
		{
			perror("get_item");
			exit(EXIT_FAILURE);
		}
		ptr = ptr->next;
	}

	return (ptr->n);
}


/**
 * get_len - get length of singly linked list
 * @head: address of the pointer to the head of the linked list
 * Return: length of list, 0 - based
 */
int get_len(listint_t **head)
{
	listint_t *ptr = *head;
	int pos = 0;

	while (ptr)  /* if you reach NULL that is the end of the list */
	{
		ptr = ptr->next;
		pos++;
	}

	return (pos);
}
