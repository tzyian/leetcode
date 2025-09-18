# @leet start
defmodule Solution do
  @spec repair_cars(ranks :: [integer], cars :: integer) :: integer
  def repair_cars(ranks, cars) do
    min_rank = Enum.min(ranks)
    left = 1
    right = min_rank * cars * cars
    binary_search(left, right, ranks, cars)
  end

  @spec can_repair?(ranks :: [integer], cars :: integer, time :: integer) :: boolean
  defp can_repair?(ranks, cars, time) do
    total_cars =
      Enum.reduce(ranks, 0, fn rank, acc ->
        (acc + :math.floor(:math.sqrt(time / rank))) |> trunc()
      end)

    total_cars >= cars
  end

  @spec binary_search(left :: integer, right :: integer, ranks :: [integer], cars :: integer) ::
          integer
  defp binary_search(left, right, _ranks, _cars) when left >= right(do: left)

  defp binary_search(left, right, ranks, cars) when left < right do
    mid = div(left + right, 2)

    if can_repair?(ranks, cars, mid) do
      binary_search(left, mid, ranks, cars)
    else
      binary_search(mid + 1, right, ranks, cars)
    end
  end
end

# @leet end

