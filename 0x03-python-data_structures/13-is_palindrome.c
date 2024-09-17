#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * add_nodeint_begin - adds node at the beginning of listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to add in listint_t list
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_begin(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}

/**
 * is_palindrome - function that checks if a singly list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: '0' if it is not a palindrome, '1' if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *second_head  = *head;
	listint_t *cpy_list = NULL, *cpy2_list = NULL;

	if (*head == NULL || second_head->next == NULL)
		return (1);
	while (second_head != NULL)
	{
		add_nodeint_begin(&cpy_list, second_head->n);
		second_head = second_head->next;
	}
	cpy2_list = cpy_list;
	while (*head != NULL)
	{
		if ((*head)->n != cpy2_list->n)
		{
			free_listint(cpy_list);
			return (0);
		}
		*head = (*head)->next;
		cpy2_list = cpy2_list->next;
	}
	free_listint(cpy_list);
	return (1);
}
